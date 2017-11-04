<template>
  <div>
    <div class="loading" v-if="loading">
      Loading...
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="movie">
      <div class="content">
        <div class="column left">
          <img :src="movie.poster_url" alt="poster" class="poster">
        </div>
        <div class="column right">
          <h2>
            <button type="button" @click="backButton">Back</button>
            <span>{{ movie.name }}</span>
          </h2>
          <div><b>Description</b>: {{movie.description}}</div>
          <div><b>Duration</b>: {{movie.duration}} m</div>
          <div><b>Ticket prive</b>: {{movie.price}}</div>
          <div><b>Genres</b>: <span class="genre" v-for="genre in movie.genres">{{genre.name}} </span></div>
          <div><b>Start at</b>: {{movie.session_start}}</div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import axios from 'axios'
  import * as Constants from './../../constants/constants'

  export default {
    name: 'Movie',
    props: ['item'],
    data () {
      return {
        loading: false,
        movie: null,
        error: null,
        id: this.$route.params.id
      }
    },
    created () {
      this.fetchData()
    },
    watch: {
      // call again the method if the route changes
      '$route': 'fetchData'
    },
    methods: {
      fetchData () {
        this.error = this.movie = null
        this.loading = true
        axios({method: 'GET', 'url': Constants.API_URL + 'movies/' + this.id})
          .then(result => {
            this.movie = result.data.movie
            this.loading = false
            document.title = document.title + ' - ' + this.movie.name
          }, error => {
            this.error = error.toString()
          })
      },
      backButton () {
        this.$router.go(-1)
      }
    }
  }
</script>

<style>
  .content {
    display: flex;
    flex-direction: row;

    justify-content: space-around;
    align-items: stretch;

    padding-top: 20px;
  }

  .column.left {
    width: 50%;
    flex: 0 50%;
  }

  .column.right {
    width: 50%;
    flex: 0 50%;
    border-left: 1px solid #eee;

    padding-left: 20px;
  }

  .column div{
    padding-top: 10px;
  }

  .poster {
    width: 100%;
    height: auto;
  }

  .genre{
     background: #423f3f;
    padding: 3px 10px;
    border: 1px solid;
    border-radius: 27%;
    margin-right: 5px;
  }
</style>
