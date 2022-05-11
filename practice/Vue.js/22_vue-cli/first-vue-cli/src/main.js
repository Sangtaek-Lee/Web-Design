import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

// 똑같은거다 하지만 완전히 똑같진 않다.
// const App = {
//   template: ''
// }
// new Vue({
//   el: "#app"
// })