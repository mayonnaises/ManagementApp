import api from '@/services/api'

const state = {
  department: []
}

const actions = {
  getDepartmentList ({ commit }) {
    return api.get('department_list/')
      .then(response => {
        commit('setDepartment', response.data)
      })
  }
}

const mutations = {
  setDepartment (state, department) {
    state.department = department
  }
}

export default {
  state,
  actions,
  mutations
}
