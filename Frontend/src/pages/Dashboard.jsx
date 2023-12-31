import { CardContent, Grid } from "@mui/material";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { useEffect, useState } from "react";
import useInterval from "../hooks/useInterval";
import SingleLineChartProd from "../components/charts/SingleLineChartProd";
import BarChartProd from "../components/charts/BarChartProd";
import PieChartAntennaFail from "../components/charts/PieChartAntennaFail";

export default function Dashboard() {
  const [flow, setFlow] = useState();
  const [estimated, setEstimated] = useState();
  const [time, setTime] = useState();

  const loadData = async () => {
    const responseNow = await fetch(
      "http://localhost:8000/wells/calculate/now"
    );
    const response_acumulated = await fetch(
      "http://localhost:8000/wells/calculate/today"
    );
    const now = await responseNow.json();
    const accum = await response_acumulated.json();
    setFlow(now[0].flow);
    const flowHours = now[0].flow / 24;
    setEstimated(
      accum[0].accumulated + flowHours * (24 - new Date().getHours())
    );
  };

  useEffect(() => {
    setTime(new Date().toLocaleTimeString());
    loadData();
  }, []);

  useInterval(loadData, 15000);

  useInterval(() => {
    setTime(new Date().toLocaleTimeString());
  }, 1000);

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={2} a>
        <Grid item xs={12} display="flex">
          <Grid item xs={4}>
            <CardContent>
              <Typography
                sx={{ fontSize: 18 }}
                color="text.secondary"
                gutterBottom
              >
                Puntual de Salida
              </Typography>
              <Typography variant="h5" component="div">
                {flow}
              </Typography>
              <Typography color="text.secondary">Sm3/d</Typography>
            </CardContent>
          </Grid>
          <Grid item xs={4}>
            <CardContent>
              <Typography
                sx={{ fontSize: 18 }}
                color="text.secondary"
                gutterBottom
              >
                Estimación al Cierre
              </Typography>
              <Typography variant="h5" component="div">
                {estimated}
              </Typography>
              <Typography color="text.secondary">Sm3/d</Typography>
            </CardContent>
          </Grid>
          <Grid item xs={4}>
            <CardContent>
              <Typography
                sx={{ fontSize: 18 }}
                color="text.secondary"
                gutterBottom
              >
                Hora
              </Typography>
              <Typography variant="h5" component="div">
                {time}
              </Typography>
              <Typography color="text.secondary"></Typography>
            </CardContent>
          </Grid>
        </Grid>
        <Grid item xs={4}>
          <Typography sx={{ fontSize: 18 }} color="text.secondary">
            Comunicación
          </Typography>
          <PieChartAntennaFail />
        </Grid>
        <Grid item xs={8}>
          <Typography sx={{ fontSize: 18 }} color="text.secondary">
            Caudal por Hora
          </Typography>
          <SingleLineChartProd />
          <br />
          <Typography sx={{ fontSize: 18 }} color="text.secondary">
            Cierre días previos en Sm3/d
          </Typography>
          <BarChartProd />
        </Grid>
      </Grid>
    </Box>
  );
}
