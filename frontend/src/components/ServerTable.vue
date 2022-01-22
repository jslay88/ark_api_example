<template>
  <div>
    <table class="table text-center">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Version</th>
          <th scope="col">Updated</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="!servers.length">
          <td colspan="3">No Servers</td>
        </tr>
        <ServerRow v-else v-for="server in servers" :key="server.id" :name="server.name" :version="server.version" :updated="server.updated"></ServerRow>
      </tbody>
    </table>

    <!-- Error Toast -->
    <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 11">
      <div ref="toast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          <strong class="me-auto">An error has occurred.</strong>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body" v-if="error !== null">
          {{ JSON.parse(error).detail }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Toast } from 'bootstrap'
import ServerRow from "@/components/ServerRow"

export default {
  components: {
    ServerRow
  },
  name: "ServerTable",
  data() {
    return {
      servers: [],
      error: null
    }
  },
  methods: {
    getServers: async function() {
      const response = await fetch('/api/v1/server/', {cache: 'no-cache'})
      if (response.status !== 200) {
        this.error = await response.text()
        console.log(this.error)
        let toast = new Toast(this.$refs.toast)
        toast.show()
        return
      }
      const data = await response.json()
      this.servers = data['servers']
    }
  },
  beforeMount() {
    this.getServers()
  }
}
</script>

<style scoped>

</style>