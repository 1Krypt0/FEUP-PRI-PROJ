<template>
  <div class="inline-block bg-slate-500 rounded-full px-3 py-1 text-sm font-semibold text-white mr-2 mb-2">
    <!-- <router-link to="/mlt" custom v-slot="{ navigate }"> -->
    <!--   <button @click="navigate" role="link"> -->
    <!--     More Like This {{ id }} -->
    <!--   </button> -->
    <!-- </router-link> -->
    <form @submit.prevent="getMoreLikeThis">
      <button role="link">
        More Like This {{ id }}
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
