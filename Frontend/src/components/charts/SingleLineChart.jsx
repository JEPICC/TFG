import { LinePlot } from "@mui/x-charts/LineChart";
import { ResponsiveChartContainer } from "@mui/x-charts/ResponsiveChartContainer";
import { useEffect, useState } from "react";
import { ChartsXAxis } from "@mui/x-charts/ChartsXAxis";
import { ChartsYAxis } from "@mui/x-charts/ChartsYAxis";
import { axisClasses } from "@mui/x-charts/ChartsAxis";
import { Box } from "@mui/material";
import { ChartsTooltip } from "@mui/x-charts/ChartsTooltip";
import { ChartsAxisHighlight } from "@mui/x-charts/ChartsAxisHighlight";

export default function SingleLineChart2(prop) {
  const [values, setValues] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/values/meter/" + prop.meter)
      .then((response) => response.json())
      .then((data) => {
        const dataPlus = data.map(({ timestamp, value }) => ({
          date: new Date(timestamp),
          value: value,
        }));
        setValues(dataPlus);
      });
  }, [prop.meter]);

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
            label: prop.uom,
            color: prop.color,
            showMark: false,
          },
        ]}
        dataset={values}
        height={400}
        margin={{ left: 100, right: 70 }}
        sx={{
          [`.${axisClasses.left} .${axisClasses.label}`]: {
            transform: "translate(-45px, 0)",
          },
        }}
      >
        <LinePlot />
        <ChartsXAxis label="Hora" />
        <ChartsYAxis label={prop.label + " en " + prop.uom} />
        <ChartsTooltip />
        <ChartsAxisHighlight x="line" />
      </ResponsiveChartContainer>
    </Box>
  );
}
