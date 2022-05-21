import Vue from 'vue'
import App from './App.vue'
import { store } from './store/store'    // export 한 걸 {} 로 접근하여 가져온다.

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store,
}).$mount('#app')
