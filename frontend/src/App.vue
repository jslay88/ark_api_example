<template>
  <div class="container py-5">
    <div class="text-center">
      <h2>Server Listings</h2>
    </div>
    <ServerTable />
  </div>
</template>

<script>
import ServerTable from "@/components/ServerTable"

export default {
  name: 'App',
  components: {
    ServerTable
  }
}
</script>

<style>
</style>
