<template>
  <div class="about">
    <h1>{{ department.name }}</h1>
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
    console.log(this.$route.params.departmentId)
    api.get('/department_detail/' + this.$route.params.departmentId)
      .then(response => {
        this.department = response.data
        console.log(this.department)
      })
  }
}
</script>
