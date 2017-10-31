<template>
  <div @mouseenter="mouseOver" @mouseleave="mouseOver" @click="onclick">
    <div class="movie-poster">
      <img :src=item.poster_url alt="">
    </div>
    <div class="movie-info">
      <div class="movie-info-name">{{item.name}}</div>
      <div class="movie-info-genres" v-show="activeInfo">
        <b>Genres:</b> <span v-for="genre in item.genres">{{genre}} </span>
      </div>
      <div class="movie-info-duration" v-show="activeInfo">
        <b>Duration:</b> {{item.duration}} m
      </div>
    </div>
    <div class="ribbon"><span>{{item.session_start}}</span></div>
  </div>

</template>

<script>
  import router from './../../router/index'
  export default {
    props: ['item'],
    name: 'MovieListItem',
    data () {
      return {
        activeInfo: false
      }
    },
    created () {
    },
    methods: {
      mouseOver: function () {
        this.activeInfo = !this.activeInfo
      },
      onclick: function () {
        console.log(this)
        router.push({ path: `/movie/${this.item.id}` })
      }
    }
  }
</script>

<style>

</style>
