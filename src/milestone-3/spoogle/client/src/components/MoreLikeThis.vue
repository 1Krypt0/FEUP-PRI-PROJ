<template>
  <span
    class="inline-block bg-slate-500 rounded-full px-3 py-1 text-sm font-semibold text-white mr-2 mb-2"
    >More Like This</span
  >
</template>

<script setup lang="ts">
export interface Article {
  id: string;
}
const props = defineProps<Article>();
</script>
