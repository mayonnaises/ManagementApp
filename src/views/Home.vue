<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <keep-alive>
      <Search msg="Hello World"/>
    </keep-alive>
  </div>
</template>

<script>
// @ is an alias to /src
import Search from '@/components/Search.vue'

export default {
  name: 'Home',
  components: {
    Search
  }
}
</script>
