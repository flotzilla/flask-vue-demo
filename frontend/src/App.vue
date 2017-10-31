<template>
  <div id="app">
    <header>
      <div class="wrapper">
        <div class="main-logo">
          <router-link class="main-logo" to="/">Ticket booking</router-link>
        </div>
        <nav>
            <router-link to="/login">Login</router-link>
        </nav>
        <div class="search-block">
          <input type="search" placeholder="search" v-model="search"/>
        </div>
      </div>
    </header>
    <main class="main-section">
      <router-view :searchable="search"></router-view>
    </main>
    <footer></footer>
  </div>
</template>

<script>
  export default {
    name: 'app',
    data () {
      return {
        search: ''
      }
    }
  }
</script>

<style>
  @import './assets/css/style.css';
</style>
