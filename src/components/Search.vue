<template>
  <div id="search_block">
    <h1>Search page</h1>
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
