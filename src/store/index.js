import { createStore } from 'vuex'
// import axios from 'axios'
import api from '@/services/api'
import employee from './modules/employee'

export default createStore({
  state: {
    department: [],
    employees: []
  },
  mutations: {
    setDepartment (state, department) {
      state.department = department
    },
    setEmployee: function (state, employees) {
      state.employees = employees
    }
  },
  actions: {
    getDepartmentList ({ commit }) {
      return api.get('department_list/')
        .then(response => {
          commit('setDepartment', response.data)
        })
    },
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
