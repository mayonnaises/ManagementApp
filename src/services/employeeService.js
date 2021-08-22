import api from '@/services/api'

export default {
  getEmployeeList () {
    return api.get('employee_list/')
      .then(response => response.data)
  }
}
