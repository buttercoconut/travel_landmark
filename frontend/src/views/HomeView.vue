<template>
  <div class="home-view">
    <h1>Landmark List</h1>
    <div v-if="landmarks.length === 0">Loading...</div>
    <div v-else>
      <LandmarkCard v-for="l in landmarks" :key="l.id" :landmark="l" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import LandmarkCard from '../components/LandmarkCard.vue';

const landmarks = ref([]);

onMounted(async () => {
  const res = await fetch('/landmarks');
  const data = await res.json();
  landmarks.value = data;
});
</script>

<style scoped>
.home-view {
  padding: 1rem;
}
</style>
