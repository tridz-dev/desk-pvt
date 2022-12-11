<template>
	<v-chart class="chart" :option="option" />
</template>

<script>
import ECharts from "vue-echarts"
import "echarts/lib/chart/bar"
import { ref } from "vue"

export default {
	components: {
		"v-chart": ECharts,
	},
	data() {
		let ticketType = []
		let ticketCount = []
		let option = {
			title: {
				text: "Tickets by Type",
				left: "center",
			},
			yAxis: {
				type: "category",
				data: ticketType,
			},
			xAxis: {
				type: "value",
			},
			series: [
				{
					data: ticketCount,
					type: "bar",
				},
			],
		}

		return {
			option,
			ticketType,
			ticketCount,
		}
	},
	methods: {
		count() {
			this.$resources.getTicketTypeCount.fetch()
		},
	},
	resources: {
		getTicketTypeCount() {
			return {
				method: "frappedesk.api.dashboard.ticket_type",
				onSuccess: (res) => {
					res.map((value) => {
						this.ticketCount.push(value.count)
						this.ticketType.push(value.ticket_type)
					})
				},
				auto: true,
			}
		},
	},
}
</script>
<style scoped>
.chart {
	height: 50vh;
}
</style>
