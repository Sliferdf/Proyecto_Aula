import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Vuetify from 'vuetify'
import AddCoworking from '@/components/Coworking/AddCoworking'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'


Vue.use(Router)
Vue.use(Vuetify, {
  iconfont: 'md'
})

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/add',
      name: 'AddCoworking',
      component: AddCoworking,
    
    }
  ]
})
