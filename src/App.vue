<template>
  <div id="nav">
    <router-link to="/">Search</router-link> |
    <router-link to="/edit">Edit</router-link> |
    <router-link to="/list">List</router-link>
  </div>
  <router-view v-slot="{ Component }">
    <keep-alive exclude="Department">
      <component :is="Component" />
    </keep-alive>
  </router-view>
</template>

<style>
* {
  margin: 0;padding: 0;
  font-size: 10px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#nav {
  padding: 25px;
}
#nav a {
  margin: 0 10px;
  font-size: 1.8rem;
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}
#nav a:hover {
  opacity: 0.6;
}
#nav a.router-link-exact-active {
  text-decoration: underline solid #42b983;
  color: #42b983;
}
</style>
