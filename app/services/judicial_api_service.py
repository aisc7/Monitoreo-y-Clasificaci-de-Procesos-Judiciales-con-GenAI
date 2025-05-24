import requests
import os
import logging
from typing import Dict, Any, Optional

class JudicialAPIService:
    """
    Servicio para interactuar con los endpoints de la Rama Judicial.
    """

    def __init__(self):
        self.base_url = os.getenv('BASE_URL', 'https://consultaprocesos.ramajudicial.gov.co:448/api/v2')
        self.logger = logging.getLogger(__name__)

    def consulta_por_nombre(self, nombre: str, tipo_persona: str, codificacion_despacho: Optional[str], pagina: int = 1, solo_activos: bool = True) -> Dict:
        endpoint = f"{self.base_url}/Procesos/Consulta/NombreRazonSocial"
        params = {
            "nombre": nombre,
            "tipoPersona": tipo_persona,
            "SoloActivos": str(solo_activos).lower(),
            "pagina": pagina
        }
        if codificacion_despacho:
            params["codificacionDespacho"] = codificacion_despacho
        return self._get(endpoint, params)

    def consulta_por_radicado(self, numero: str, pagina: int = 1, solo_activos: bool = False) -> Dict:
        endpoint = f"{self.base_url}/Procesos/Consulta/NumeroRadicacion"
        params = {
            "numero": numero,
            "SoloActivos": str(solo_activos).lower(),
            "pagina": pagina
        }
        return self._get(endpoint, params)

    def consulta_detalle_proceso(self, id_proceso: str) -> Dict:
        endpoint = f"{self.base_url}/Proceso/Detalle/{id_proceso}"
        return self._get(endpoint)

    def consulta_actuaciones_proceso(self, id_proceso: str) -> Dict:
        endpoint = f"{self.base_url}/Proceso/Actuaciones/{id_proceso}"
        return self._get(endpoint)

    def consulta_documentos_actuacion(self, id_reg_actuacion: str) -> Dict:
        endpoint = f"{self.base_url}/Proceso/DocumentosActuacion/{id_reg_actuacion}"
        return self._get(endpoint)

    def descarga_documento(self, id_reg_documento: str) -> bytes:
        endpoint = f"{self.base_url}/Descarga/Documento/{id_reg_documento}"
        return self._get(endpoint, raw_response=True)

    def _get(self, endpoint: str, params: Optional[Dict] = None, raw_response: bool = False) -> Any:
        try:
            self.logger.info(f"GET {endpoint} con params {params}")
            response = requests.get(endpoint, params=params, timeout=30)
            response.raise_for_status()
            return response.content if raw_response else response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error al consultar {endpoint}: {e}")
            raise Exception(f"Error en la petición a la API Judicial: {e}")
