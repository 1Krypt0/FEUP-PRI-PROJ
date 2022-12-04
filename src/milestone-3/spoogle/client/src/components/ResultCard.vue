<script setup lang="ts">
import { computed } from "vue";
import ResultTagSection from "./ResultTagSection.vue";
export interface Article {
  id: string;
  title: string;
  url: string;
  content: string;
  author: string;
  date: string;
  tags: string[];
  sections: string[];
}
const props = defineProps<Article>();
const prettyDate = computed(() => {
  return new Date(props.date).toLocaleDateString(undefined, {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
});
</script>

<template>
  <section class="max-w-full rounded overflow-hidden shadow-lg">
    <div class="px-6 py-4 max-w-full">
      <div class="font-bold text-xl mb-2">
        <RouterLink :to="{ name: 'result', params: { id: id ? id : 0 } }">
          {{ title }}
        </RouterLink>
      </div>
      <p class="text-gray-700 text-base max-w-[100ch] truncate">
        {{ content }}
      </p>
    </div>

    <div class="px-6 flex items-center">
      <div class="text-sm">
        <p class="text-gray-900 leading-none">{{ author }}</p>
        <p class="text-gray-600">{{ prettyDate }}</p>
      </div>
    </div>

    <div class="px-6 pt-4 pb-2">
      <ResultTagSection
        v-for="tag of tags"
        :key="tag"
        :content="tag"
        :is-tag="true"
      />
      <ResultTagSection
        v-for="section of sections"
        :key="section"
        :content="section"
        :is-tag="false"
      />
    </div>
  </section>
</template>
