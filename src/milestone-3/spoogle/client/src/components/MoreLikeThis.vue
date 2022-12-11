<template>
  <div class="">
    <form @submit.prevent="getMoreLikeThis">
      <button class="text-sm underline underline-offset-2 text-slate-600" role="link">
        More like this
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

export interface Article {
  id: string;
}
const props = defineProps<Article>();
const router = useRouter()
function getMoreLikeThis() {
  router.push({name: "mlt", query: {id: props.id}});
}


</script>
