import { LinePlot } from "@mui/x-charts/LineChart";
import { ResponsiveChartContainer } from "@mui/x-charts/ResponsiveChartContainer";
import { useEffect, useState } from "react";
import { ChartsXAxis } from "@mui/x-charts/ChartsXAxis";
import { ChartsYAxis } from "@mui/x-charts/ChartsYAxis";
import { axisClasses } from "@mui/x-charts/ChartsAxis";
import { Box } from "@mui/material";
import { ChartsTooltip } from "@mui/x-charts/ChartsTooltip";
import { ChartsAxisHighlight } from "@mui/x-charts/ChartsAxisHighlight";

export default function SingleLineChartProd() {
  const [values, setValues] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/wells/calculate/todayHours")
      .then((response) => response.json())
      .then((data) => {
        const dataPlus = data.map((item) => ({
          date: new Date(item._id.date),
          value: item.acumm,
        }));
        setValues(dataPlus);
      });
  }, []);

  if (values.length == 0) return "";

  return (
    <Box sx={{ width: "100%" }}>
      <ResponsiveChartContainer
        xAxis={[
          {
            dataKey: "date",
            scaleType: "time",
          },
        ]}
        series={[
          {
            type: "line",
            dataKey: "value",
            label: "Sm3/d",
            color: 'orange',
            showMark: false,
          },
        ]}
        dataset={values}
        height={300}
        margin={{ left: 100, right: 70 }}
        sx={{
          [`.${axisClasses.left} .${axisClasses.label}`]: {
            transform: "translate(-45px, 0)",
          },
        }}
      >
        <LinePlot />
        <ChartsXAxis label="Hora" />
        <ChartsYAxis label="Caudal en Sm3/d" />
        <ChartsTooltip />
        <ChartsAxisHighlight x="line" />
      </ResponsiveChartContainer>
    </Box>
  );
}
