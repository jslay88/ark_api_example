<template>
  <tr>
    <td>{{ name }}</td>
    <td>{{ version }}</td>
    <td>{{ moment(`${updated}Z`).fromNow() }}</td>
  </tr>
</template>

<script>
import moment from 'moment'

export default {
  name: 'ServerRow',
  props: {
    name: String,
    version: String,
    updated: String
  },
  data() {
    return {
      moment: moment
    }
  }
}
</script>

<style scoped>
</style>
