<template>
  <span
    v-if="isTag"
    class="inline-block bg-snblack rounded-full px-3 py-1 text-sm font-semibold text-white mr-2 mb-2"
    >{{ content }}</span
  >
  <span
    v-else
    class="inline-block bg-snred rounded-full px-3 py-1 text-sm font-semibold text-white mr-2 mb-2"
    >{{ content }}</span
  >
</template>

<script setup lang="ts">
export interface Tag {
  isTag: boolean;
  content: string;
}
const props = defineProps<Tag>();
</script>
