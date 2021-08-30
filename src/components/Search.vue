<template>
  <div id="search_block">
    <h1>Search page</h1>
    <div>
      <div class="radio-wrapper">
        <input
          type="radio"
          id="department_radio"
          name="search_model"
          value="department"
          checked />
        <label for="department_radio" class="search-choice-label">Department</label>
      </div>
      <div class="radio-wrapper">
        <input
          type="radio"
          id="employee_radio"
          name="search_model"
          value="employee" />
        <label for="employee_radio" class="search-choice-label">Employee</label>
      </div>
    </div>
    <div id="search_app">
      <form id="search_form">
        <input
          type="text"
          v-model="searchResult"
          id="search_input"
          ref="get_user_input_window" />
        <button type="submit" id="search_submit">Search</button>
      </form>
    </div>
  </div>
  <div id="search_result"
    v-for="data in searchResult"
    :key="data.id">
    <p class="result-name">{{ data.name }}</p>
  </div>
</template>

<script>
export default {
  name: 'Search',
  props: {
    msg: String
  },
  data () {
    return {
      employeeData: [],
      searchResult: []
    }
  },
  watch: {
    searchResult (inputText, oldText) {
      console.log(inputText)
      const resultsList = this.employeeData.filter(user => {
        return user.name.includes(inputText)
      })
      console.log(resultsList)
    }
  },
  methods: {
    filterTheData (userInput) {
      const resultsList = this.employeeData.filter(user => {
        return user.name.includes(userInput)
      })
      this.searchResult = resultsList
    }
  },
  mounted () {
    this.$store.dispatch('getEmployeeList')
    this.employeeData = this.$store.state.employees

    this.$refs.get_user_input_window.focus()
    console.log(this.employeeData)
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
a {
  color: #42b983;
}
</style>
