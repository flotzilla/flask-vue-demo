<template>
  <div>
    <div>Movie #{{ $route.params.id }}</div>
  </div>

</template>

<script>
  export default {
    name: 'Movie',
    props: ['item'],
    created () {
      console.log(this)
//      console.log(this.route)
    }

  }
</script>

<style>
</style>
