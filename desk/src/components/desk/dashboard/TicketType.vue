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
		let ticketCount = []
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
				top: "bottom",
			},
			series: [
				{
					name: "Feedback Status",
					type: "pie",
					radius: "50%",
					data: ticketCount,
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
			ticketCount,
		}
	},

	methods: {
		count() {
			this.$resources.getFeedbackStatusCount.fetch()
		},
	},
	resources: {
		getFeedbackStatusCount() {
			return {
				method: "frappedesk.api.dashboard.feedback_status",
				onSuccess: (res) => {
					res.map((value) => {
						this.ticketCount.push(value)
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
