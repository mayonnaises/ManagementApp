<template>
  <div class="list">
    <h1>List page</h1>
    <div v-for="employee in $store.state.employees" :key="employee.id">
      <p class="em-name">{{ employee.name }}</p>
      <p class="em-phone">{{ employee.phone_number }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'List',
  computed: {
    employees: function () {
      return this.$store.state.employees
    }
  },
  mounted () {
    this.$store.dispatch('getEmployeeList')
  }
}
</script>

<style scoped>
.em-name {
  font-size: 16px;
  color: #111;
}
</style>
