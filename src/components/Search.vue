<template>
  <div id="search_block">
    <form id="search_form">
      <input type="text" id="search_input" />
      <button type="submit" id="search_submit">Search</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Search',
  props: {
    msg: String
  }
}
</script>

<style scoped>
#search_input {
  padding: 4px 6px;
  font-size: 15px;
  font-weight: 600;
  color: #333;
}
#search_submit {
  padding: 4px 3px;
  font-size: 15px;
  color: #333;
  border-radius: 0;
}
a {
  color: #42b983;
}
</style>
