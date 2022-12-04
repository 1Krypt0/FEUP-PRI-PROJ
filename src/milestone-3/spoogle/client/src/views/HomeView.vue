<template>
  <main class="flex items-center justify-center">
    <section class="flex flex-col justify-evenly pb-32 w-1/4 h-3/4">
      <img src="../assets/logo.svg" class="w-" />
      <SearchBox :query="''" />
    </section>
  </main>
</template>

<script setup lang="ts">
import SearchBox from "../components/SearchBox.vue";
</script>
