<template>
	<v-chart class="chart" :option="option" :init-options="initOptions" />
</template>

<script>
import { use } from "echarts/core"
import { CanvasRenderer } from "echarts/renderers"
import { BarChart, LineChart } from "echarts/charts"
import {
	TitleComponent,
	GridComponent,
	TooltipComponent,
	LegendComponent,
} from "echarts/components"
import VChart from "vue-echarts"

use([
	CanvasRenderer,
	BarChart,
	LineChart,
	TitleComponent,
	TooltipComponent,
	LegendComponent,
	GridComponent,
])

export default {
	name: "TicketTrends",
	components: {
		VChart,
	},
	data() {
		let data = [
			{ date: "20/6", replied: 2, resolved: 2, open: 2 },
			{ date: "22/6", replied: 2, resolved: 4, open: 5 },
		]
		const option = {
				title: {
					text: "Tickets Summary",
					left: "center",
				},
				xAxis: {
					data: ["24/6", "25/6", "26/6", "27/6", "28/6", "29/6"],
				},
				yAxis: { type: "value" },
				series: [
					{
						type: "line",
						data: [23, 24, 18, 22, 27, 29, 30, 31],
					},
					{
						type: "line",
						data: [29, 26, 34, 22, 18, 26, 25, 20],
					},
					{
						type: "line",
						data: [27, 28, 25, 26, 27, 28, 29, 30],
					},
				],
			},
			initOptions = {
				renderer: option.renderer || "canvas",
			}

		return {
			option,
			initOptions,
		}
	},

	methods: {
		getStatus() {
			console.log(this.$resources.ticketStatus.fetch())
			this.$resources.ticketStatus.fetch()
		},
	},

	resources: {
		ticketStatus() {
			return {
				method: "frappedesk.api.dashboard.ticket_status",
				onSuccess: (res) => {
					console.log(res)
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
