<template>
  <div id="app">
    <header>
      <nav>
        <div>
          <router-link to="/">Main</router-link>
          <router-link to="/login">Login</router-link>
          <!--<a @click="login" >Login</a>-->
        </div>
      </nav>
    </header>
    <main class="main-section">
      <router-view/>
    </main>
    <footer></footer>
  </div>
</template>

<script>
  export default {
    name: 'app',
    methods: {
    }
  }
</script>

<style>
  @import './assets/css/style.css';
</style>
