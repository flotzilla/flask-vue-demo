<template>
  <div class="movie-list-wrapper">
    <!--<router-link to="/movie/12">asdasd</router-link>-->
    <div class="genres-list">
      <ul>
        <li v-for="filter in filters" @click="selectFilter(filter)" :class="{ filterActive: activeFilter === filter }">
          {{filter}}
        </li>
      </ul>
    </div>

    <div class="loading" v-if="loading">
      Loading...
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div class="movie-list" v-if="movies">
      <MovieListItem v-for="item in filteredList"
                     :key="item.id" :item="item" class="movie-list-item"></MovieListItem>
    </div>


  </div>
</template>

<script>
  import MovieListItem from './MovieListItem.vue'
  import axios from 'axios'
  import * as Constants from './../../constants/constants'

  export default {
    name: 'MoviesList',
    props: ['searchable'],
    components: {
      MovieListItem: MovieListItem
    },
    data () {
      return {
        activeFilter: 'all',
        filters: ['all'],
        loading: false,
        movies: [],
        error: null
      }
    },

    computed: {
      filteredList: function () {
        let self = this
        let filtered = this.movies
        if (this.searchable.length > 0) {
          filtered = this.movies.filter((item) => {
            return item.name.toLowerCase().includes(this.searchable.toLowerCase())
          })
        }

        if (this.activeFilter === 'all') {
          return filtered
        }

        filtered = filtered.filter(item => {
          return item.genres.find((val) => {
            return val.name === self.activeFilter
          })
        })
        return filtered
      }
    },

    methods: {
      selectFilter: function (filter) {
        this.activeFilter = filter
      },
      getMovies () {
        this.error = this.movies = null
        this.loading = true
        axios({method: 'GET', 'url': Constants.API_URL + 'movies'})
          .then(result => {
            this.movies = result.data.movies
            this.loading = false
          }, error => {
            this.error = error.toString()
          })
      },
      getGenres () {
        axios({method: 'GET', 'url': Constants.API_URL + 'genres'})
          .then(result => {
            if (result.data.genres.length > 0) {
              this.parseGenres(result.data.genres)
            }
          }, error => {
            this.loading = false
            this.error = error.toString()
          })
      },
      parseGenres (list) {
        let filters = ['all']
        list.forEach(function (el) {
          filters.push(el.name)
        })
        this.filters = filters
        console.log(this.filters)
      }
    },
    created () {
      this.getMovies()
      this.getGenres()
    }
  }
</script>

<style>
  .error{
      text-align: center;
      font-size: 2em;
  }
</style>
