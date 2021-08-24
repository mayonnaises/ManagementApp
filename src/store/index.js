import { createStore } from 'vuex'
// import axios from 'axios'
import api from '@/services/api'
import employee from './modules/employee'

export default createStore({
  state: {
    employees: []
  },
  mutations: {
    setEmployee: function (state, employees) {
      state.employees = employees
    }
  },
  actions: {
    getEmployeeList: function ({ commit }) {
      return api.get('/employee_list/')
        .then(response => {
          commit('setEmployee', response.data)
        })
    }
  },
  modules: {
    employee
  }
})
