<template>
	<div class="mt-8 ml-8 mb-8">
		<div class="line-clamp-1 text-xl text-gray-900 font-semibold">
			SLA Summary
		</div>
		<div class="grid grid-cols-3 mt-8 mb-8">
			<div
				class="flex flex-row box-border h-16 w-96 p-4 border-2 rounded-md justify-between"
			>
				<div class="font-light">Avg. First Response time (hours)</div>
				<div class="font-semibold text-3xl">
					{{ averageFirstResponseTime }}
				</div>
			</div>
			<div
				class="flex flex-row box-border h-16 w-96 p-4 border-2 rounded-md justify-between"
			>
				<div class="font-light">Avg. Resolution Time (hours)</div>
				<div class="font-semibold text-3xl">
					{{ averageResolutionTime }}
				</div>
			</div>
			<div
				class="box-border h-16 w-96 p-4 border-2 rounded-md justify-between"
			>
				Resolution within SLA
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "SlaSummary",
	computed: {
		averageFirstResponseTime() {
			return this.$resources.averageFirstResponseTime.data.toFixed(1)
		},

		averageResolutionTime() {
			return this.$resources.averageResolutionTime.data.toFixed(1)
		},
	},
	resources: {
		averageFirstResponseTime() {
			return {
				method: "frappedesk.api.dashboard.average_first_response_time",
				auto: true,
			}
		},
		averageResolutionTime() {
			return {
				method: "frappedesk.api.dashboard.average_resolution_time",
				auto: true,
			}
		},
	},
}
</script>

<style scoped></style>
