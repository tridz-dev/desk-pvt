<template>
	<v-chart class="chart" :option="option" />
</template>

<script>
import ECharts from "vue-echarts"
import "echarts/lib/chart/pie"
import "echarts/lib/component/polar"

export default {
	components: {
		"v-chart": ECharts,
	},
	data() {
		let option = {
			title: {
				text: "Customer Satisfaction Feedback",
				left: "center",
			},
			tooltip: {
				trigger: "item",
			},
			legend: {
				orient: "horizontal",
				top:"bottom"
			},
			series: [
				{
					name: "Access From",
					type: "pie",
					radius: "50%",
					data: [
						{ value: 20, name: "Positive" },
						{ value: 10, name: "Neutral" },
						{ value: 5, name: "Negative" },
					],
					emphasis: {
						itemStyle: {
							shadowBlur: 10,
							shadowOffsetX: 0,
							shadowColor: "rgba(0, 0, 0, 0.5)",
						},
					},
				},
			],
		}

		return {
			option,
		}
	},
}
</script>

<style scoped>
.chart {
	height: 50vh;
}
</style>
