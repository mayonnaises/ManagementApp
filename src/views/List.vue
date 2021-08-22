<template>
  <div class="list">
    <h1>List page</h1>

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
