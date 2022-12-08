<template>
	<v-chart class="chart" :option="option" :init-options="initOptions" />
</template>

<script>
import { use } from "echarts/core"
import { CanvasRenderer } from "echarts/renderers"
import { BarChart } from "echarts/charts"
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
		const option = {
				xAxis: {
					data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
				},
				yAxis: {},
				series: [
					{
						type: "bar",
						data: [23, 24, 18, 25, 27, 28, 25],
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
		getContacts() {},
	},
}
</script>

<style scoped>
.chart {
	height: 50vh;
}
</style>
