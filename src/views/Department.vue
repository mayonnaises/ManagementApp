<template>
  <div class="about">
    <p id="dep_name_reading">{{ department.name_reading }}</p>
    <h1 id="dep_name">{{ department.name }}</h1>
    <div class="em-info">
      <p>代表：</p>
      <p>{{ department.employee_name }}</p>
    </div>
    <div>
      <p>{{ department.employee_phone }}</p>
    </div>
    <div class="dep-info">
      <p>固定電話：</p>
      <p>{{ department.phone_number }}</p>
    </div>
    <div class="dep-info">
      <p>社内電話：</p>
      <p>{{ department.second_phone }}</p>
    </div>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'Department',
  data () {
    return {
      department: []
    }
  },
  mounted () {
    api.get('/department_detail/' + this.$route.params.departmentId)
      .then(response => {
        this.department = response.data
      })
  }
}
</script>

<style scoped>
p {
  display: inline-block;
  font-size: 1.7rem;
}
#dep_name_reading {
  margin: 10px 0 2px;
  font-size: 1.4rem;
  color: #333;
}
#dep_name {
  font-size: 2.5rem;
  color: #333;
}
.em-info {
  margin: 20px 0 5px;
}
.dep-info {
  margin: 20px 0 0;
}
</style>
