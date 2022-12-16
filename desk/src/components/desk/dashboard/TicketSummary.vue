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
	name: "TicketSummary",
	components: {
		VChart,
	},
	props: {
		props: {
			fromDate: {
				type: String,
				required: true,
			},
			toDate: {
				type: String,
				required: true,
			},
		},
		watch: {
			fromDate(newVal, Oldval) {
				console.log(newVal, Oldval, "hehehehheheh")
			},
			toDate(newVal, oldVal) {
				console.log(oldVal, newVal)
			},
		},
	},
	data() {
		let dates = []
		let open = []
		let closed = []
		let replied = []
		const option = {
				title: {
					text: "Tickets Summary",
					left: "center",
				},
				tooltip: {
					trigger: "axis",
				},
				xAxis: {
					type: "category",
					data: dates,
				},
				yAxis: { type: "value" },
				series: [
					{
						type: "line",
						data: open,
					},
					{
						type: "line",
						data: closed,
					},
					{
						type: "line",
						data: replied,
					},
				],
			},
			initOptions = {
				renderer: option.renderer || "canvas",
			}

		return {
			option,
			initOptions,
			dates,
			open,
			closed,
			replied,
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
				method: "frappedesk.api.dashboard.ticket_summary",
				params: {
					startDate: this.fromDate,
					endDate: this.toDate,
				},
				onSuccess: (res) => {
					res.map((values) => {
						this.dates.push(values[0])
						this.open.push(values[1])
						this.closed.push(values[2])
						this.replied.push(values[3])
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
