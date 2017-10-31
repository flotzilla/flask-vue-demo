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

    <div class="movie-list">
      <MovieListItem v-for="item in filteredList"
                     :key="item.id" :item="item" class="movie-list-item"></MovieListItem>
    </div>


  </div>
</template>

<script>
  import MovieListItem from './MovieListItem.vue'

  export default {
    name: 'MoviesList',
    props: ['searchable'],
    components: {
      MovieListItem: MovieListItem
    },
    data () {
      return {
        activeFilter: 'all',
        filters: ['all', 'action', 'drama', 'comedy', 'crime'],
        items: [
          {
            id: 1,
            name: 'Sunrise',
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
            name: 'Key Largo',
            description: 'Grate successor of original Blade runner movie',
            price: 12.50,
            genres: ['action', 'drama', 'comedy', 'crime', 'crime', 'crime', 'crime'],
            poster_url: 'http://lorempixel.com/250/400/',
            duration: 120,
            session_date: new Date(),
            session_start: '21.10'
          },
          {
            id: 3,
            name: 'L. A. Confidential',
            description: 'Grate successor of original Blade runner movie',
            price: 12.50,
            genres: ['comedy'],
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
            genres: ['drama'],
            poster_url: 'http://lorempixel.com/250/400/',
            duration: 120,
            session_date: new Date(),
            session_start: '21.10'
          }
        ]
      }
    },

    computed: {
      filteredList: function () {
        let self = this
        let filtered = this.items
        if (this.searchable.length > 0) {
          filtered = this.items.filter((item) => {
            return item.name.toLowerCase().includes(this.searchable.toLowerCase())
          })
        }

        if (this.activeFilter === 'all') {
          return filtered
        }

        filtered = filtered.filter(item => {
          return item.genres.find((val) => {
            return val === self.activeFilter
          })
        })
        return filtered
      }
    },

    methods: {
      selectFilter: function (filter) {
        this.activeFilter = filter
      }
    },
    created: function () {
    }
  }
</script>

<style>
</style>
