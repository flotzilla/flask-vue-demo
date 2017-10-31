<template>
  <div class="movie-list-wrapper">
    <!--<router-link to="/movie/12">asdasd</router-link>-->
    <div class="genres-list">
      <ul>
        <li>All</li>
        <li>Comedy</li>
        <li>Drama</li>
        <li>Action</li>
        <li>Adventure</li>
        <li>Crime</li>
      </ul>
    </div>

    <div class="movie-list">
      <MovieListItem v-for="item in items" :key="item.id" :item="item" class="movie-list-item"></MovieListItem>
    </div>


  </div>
</template>

<script>
  import MovieListItem from './MovieListItem.vue'

  export default {
    name: 'MoviesList',
    components: {
      MovieListItem: MovieListItem
    },
    data () {
      return {
        items: [
          {
            id: 1,
            name: 'Blade runner 2049',
            description: 'Grate successor of original Blade runner movie',
            price: 12.50,
            genres: ['action', 'drama'],
            poster_url: 'http://lorempixel.com/250/400/',
            duration: 120,
            session_date: new Date(),
            session_start: '21:10',
            active: true
          },
          {
            id: 2,
            name: 'Blade runner 2049',
            description: 'Grate successor of original Blade runner movie',
            price: 12.50,
            genres: ['action', 'drama', 'comedey', 'crime', 'crime', 'crime', 'crime'],
            poster_url: 'http://lorempixel.com/250/400/',
            duration: 120,
            session_date: new Date(),
            session_start: '21.10'
          },
          {
            id: 3,
            name: 'Blade runner 2049',
            description: 'Grate successor of original Blade runner movie',
            price: 12.50,
            genres: ['action', 'drama'],
            poster_url: 'http://lorempixel.com/250/400/',
            duration: 120,
            session_date: new Date(),
            session_start: '21.10'
          },
          {
            id: 4,
            name: 'Blade runner 2049',
            description: 'Grate successor of original Blade runner movie',
            price: 12.50,
            genres: ['action', 'drama'],
            poster_url: 'http://lorempixel.com/250/400/',
            duration: 120,
            session_date: new Date(),
            session_start: '21.10'
          },
          {
            id: 12,
            name: 'Blade runner 2049',
            description: 'Grate successor of original Blade runner movie',
            price: 12.50,
            genres: ['action', 'drama'],
            poster_url: 'http://lorempixel.com/250/400/',
            duration: 120,
            session_date: new Date(),
            session_start: '21.10'
          }
        ]
      }
    },

    created: function () {
    }
  }
</script>

<style>
</style>
