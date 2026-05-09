<template>
  <div class="detail-view">
    <h1>{{ landmark.name }}</h1>
    <p>{{ landmark.description }}</p>
    <p>Rating: {{ landmark.review_score }} / 5</p>
    <p>Location: {{ landmark.latitude }}, {{ landmark.longitude }}</p>
    <a :href="`https://www.google.com/maps/search/?api=1\u0026query=${landmark.latitude},${landmark.longitude}`" target="_blank">Open in Google Maps</a>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const landmark = ref({});

onMounted(async () => {
  const id = route.params.id;
  const res = await fetch(`/landmarks/${id}`);
  landmark.value = await res.json();
});
</script>

<style scoped>
.detail-view {
  padding: 1rem;
}
</style>
