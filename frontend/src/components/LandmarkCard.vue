<template>
  <div class="landmark-card">
    <h3>{{ landmark.name }}</h3>
    <p>{{ landmark.description }}</p>
    <p>Rating: {{ landmark.review_score }} / 5</p>
    <a :href="`https://www.google.com/maps/search/?api=1&query=${landmark.latitude},${landmark.longitude}`" target="_blank">View on Map</a>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({
  landmark: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
.landmark-card {
  border: 1px solid #ddd;
  padding: 1rem;
  margin: 0.5rem;
  border-radius: 4px;
}
</style>
