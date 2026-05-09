<template>
  <div class="plan-view">
    <h1>Travel Plan</h1>
    <form @submit.prevent="submitPlan">
      <label for="startDate">Start Date:</label>
      <input type="date" id="startDate" v-model="startDate" required />
      <label for="endDate">End Date:</label>
      <input type="date" id="endDate" v-model="endDate" required />
      <button type="submit">Generate Plan</button>
    </form>
    <div v-if="plan.length > 0">
      <h2>Suggested Itinerary</h2>
      <ol>
        <li v-for="(item, idx) in plan" :key="idx">
          {{ item.date }}: {{ item.landmark.name }}
        </li>
      </ol>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const startDate = ref('');
const endDate = ref('');
const plan = ref([]);

const submitPlan = async () => {
  const res = await fetch('/travel-plan', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ startDate: startDate.value, endDate: endDate.value }),
  });
  plan.value = await res.json();
};
</script>

<style scoped>
.plan-view {
  padding: 1rem;
}
</style>
