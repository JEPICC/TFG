/* eslint-disable react/prop-types */
import * as React from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import { Typography } from "@mui/material";

export default function WellDialog(props) {
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const descriptionElementRef = React.useRef(null);
  React.useEffect(() => {
    if (open) {
      const { current: descriptionElement } = descriptionElementRef;
      if (descriptionElement !== null) {
        descriptionElement.focus();
      }
    }
  }, [open]);

  return (
    <React.Fragment>
      <Button onClick={handleClickOpen}>Información de Pozo</Button>
      <Dialog
        open={open}
        onClose={handleClose}
        scroll={"paper"}
        aria-labelledby="scroll-dialog-title"
        aria-describedby="scroll-dialog-description"
      >
        <DialogTitle id="scroll-dialog-title">{props.well.sigla}</DialogTitle>
        <DialogContent dividers={scroll === "paper"}>
          <DialogContentText
            id="scroll-dialog-description"
            ref={descriptionElementRef}
            tabIndex={-1}
            sx={{ px: 5 }}
          >
            <Typography variant="h6" component="h4">
              Area:
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.area}</Typography>
            <Typography variant="h6" component="h2">
              Código de Area
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.cod_area}</Typography>
            <Typography id="spring-modal-title" variant="h6" component="h2">
              Empresa{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.empresa}</Typography>
            <Typography variant="h6" component="h2">
              Yacimiento:
            </Typography>

            <Typography sx={{ mb: 1 }}>{props.well.yacimiento}</Typography>
            <Typography variant="h6" component="h2">
              Código de Yacimiento{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.cod_yacimiento}</Typography>
            <Typography variant="h6" component="h2">
              Formación{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.formacion}</Typography>
            <Typography variant="h6" component="h2">
              Cuenca{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.cuenca}</Typography>
            <Typography variant="h6" component="h2">
              Provincia{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.provincia}</Typography>
            <Typography variant="h6" component="h2">
              Profundidad{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>
              {props.well.profundidad} Metros
            </Typography>
            <Typography variant="h6" component="h2">
              Tipo de Pozo{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.tipopozo}</Typography>
            <Typography variant="h6" component="h2">
              Tipo de Extracción{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.tipoextraccion}</Typography>
            <Typography variant="h6" component="h2">
              Estado{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>{props.well.tipoestado}</Typography>
            <Typography variant="h6" component="h2">
              Fecha de Incio de Perforación{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>
              {new Date(props.well.fecha_inicio_perf).toLocaleDateString()}
            </Typography>
            <Typography variant="h6" component="h2">
              Fecha de Fin de Perforación{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>
              {new Date(props.well.fecha_fin_perf).toLocaleDateString()}
            </Typography>
            <Typography variant="h6" component="h2">
              Fecha de Inicio de Producción{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>
              {new Date(props.well.fecha_inicio_prod).toLocaleDateString()}
            </Typography>
            <Typography variant="h6" component="h2">
              Fecha de Fin de Producción{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>
              {props.well.fecha_fin_prod
                ? new Date(props.well.fecha_fin_prod).toLocaleDateString()
                : " Sin Fecha "}
            </Typography>
            <Typography variant="h6" component="h2">
              Posición{" "}
            </Typography>
            <Typography sx={{ mb: 1 }}>
              {"Latitud: " + props.well.geojson.latitude}
            </Typography>
            <Typography sx={{ mb: 1 }}>
              {"Longitud: " + props.well.geojson.longitude}
            </Typography>
          </DialogContentText>
        </DialogContent>
      </Dialog>
    </React.Fragment>
  );
}
