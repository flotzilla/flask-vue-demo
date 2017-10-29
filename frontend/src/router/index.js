import Vue from 'vue'
import Router from 'vue-router'
import MoviesList from '@/components/user/MoviesList'
import Movie from '@/components/user/Movie'
import Login from '@/components/Login'
import {APP_NAME} from '@/constants/constants'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Movies',
      component: MoviesList,
      meta: {title: 'Movies List'}
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {title: 'Login'}
    },
    {
      path: '/movie/:id',
      name: 'Movie',
      component: Movie
      // meta: {title: 'Movie name'}
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.hasOwnProperty('meta') && to.meta.hasOwnProperty('title')) {
    document.title = to.meta.title
  } else {
    document.title = APP_NAME
  }
  next()
})

export default router
