<template>
  <div id="search_block">
    <div>
      <div class="radio-wrapper">
        <input
          type="radio"
          id="department_radio"
          name="search_model"
          value="department"
          v-model="picked"
          @click="changeHolder"
          checked />
        <label for="department_radio" class="search-choice-label">Department</label>
      </div>
      <div class="radio-wrapper">
        <input
          type="radio"
          id="employee_radio"
          name="search_model"
          value="employee"
          v-model="picked"
          @click="changeHolder" />
        <label for="employee_radio" class="search-choice-label">Employee</label>
      </div>
    </div>
    <div id="search_app">
      <form id="search_form">
        <input
          type="text"
          v-model.trim="searchWord"
          id="search_input"
          ref="get_user_input_window"
          placeholder="Enter the department name here ..." />
      </form>
    </div>
  </div>
  <div id="result_table_heading">
    <p class="table-heading-content">Name</p>
    <p class="table-heading-content">Phone number</p>
    <p class="table-heading-content">Representative</p>
  </div>
  <div id="search_result_table">
    <div class="results-grid"
      v-for="data in searchData"
      :key="data.id">
      <p class="data-box data-name" v-html="highLight(data.name)"></p>
      <p class="data-box phone" v-html="highLight(data.phone_number)"></p>
      <p class="data-box" v-html="highLight(data.employee_name)"></p>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Search',
  props: {
    msg: String
  },
  data () {
    return {
      searchWord: '',
      picked: 'department'
    }
  },
  computed: {
    searchData: function () {
      const word = this.searchWord

      if (word === '') return this.department

      if (this.picked === 'department') {
        return this.department.filter(data => {
          return data.name.includes(word)
        })
      } else {
        return this.department.filter(data => {
          return data.employee_name.includes(word)
        })
      }
    },
    ...mapState(['employees', 'department'])
  },
  methods: {
    highLight (text) {
      const word = this.searchWord

      if (word === '') return text
      if (!text.includes(word)) return text

      const re = new RegExp(word, 'ig')

      return text.replace(re, function (searchWord) {
        return '<span style="background-color:yellow;font-weight:bold">' +
          searchWord +
          '</span>'
      })
    },
    changeHolder: function (event) {
      const choice = event.target.value

      if (choice === 'department') {
        this.$refs.get_user_input_window.placeholder = 'Enter the department name here ...'
      } else {
        this.$refs.get_user_input_window.placeholder = 'Enter the employee name here ...'
      }
    }
  },
  mounted () {
    this.$store.dispatch('getDepartmentList')
    this.$store.dispatch('getEmployeeList')

    this.$refs.get_user_input_window.focus()
  }
}
</script>

<style scoped>
.radio-wrapper {
  display: inline-block;
  margin: 0 15px 0;
}
.search-choice-label {
  font-size: 16.5px;
}
#search_form { margin: 25px 0 0; }
#search_input {
  width: 480px;
  padding: 7px 8px;
  font-size: 17px;
  font-weight: 600;
  color: #333;
}
#search_input:focus {
  border: none;
}
#search_submit {
  margin-left: 8px;
  padding: 8px 5px;
  font-size: 17px;
  color: #333;
  border-radius: 0;
}
#result_table_heading {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  height: 50px;width: 90%;
  margin: 30px 5% 0;
  background: lightgreen;
}
#search_result_table {
  width: 90%;
  margin: 0 5%;
}
.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  border-bottom: 1px solid #bababa;
}
.data-box {
}
a {
  color: #42b983;
}
</style>
