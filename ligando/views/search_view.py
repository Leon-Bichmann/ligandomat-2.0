from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import func, distinct, String
import simplejson as json

from ligando.models import (
    DBSession,
    Source,
    MsRun,
    Protein,
    HlaType,
    t_hla_map,
    SpectrumHit,
    t_spectrum_protein_map, PeptideRun)
from ligando.views.view_helper import conn_err_msg, js_list_creator, js_list_creator_dataTables


@view_config(route_name='search', renderer='../templates/search_result.pt', request_method="POST")
def search_result(request):
    # try:
    result = dict()
    # Search SpectrumHit Sequence
    result["peptide"] = json.dumps(DBSession.query(PeptideRun.sequence.distinct().label('peptide')).join(MsRun).filter(
        PeptideRun.sequence == request.params["search_all"]).filter(MsRun.flag_trash==0).filter(PeptideRun.source_source_id != None).all())

    # Search source columns
    result["patient_id"] = json.dumps(DBSession.query(Source.patient_id.distinct().label('source')).filter(
        Source.patient_id == request.params["search_all"]).all())
    result["dignity"] = json.dumps(DBSession.query(Source.dignity.distinct().label('dignity')).filter(
        Source.dignity == request.params["search_all"]).all())
    result["histology"] = json.dumps(DBSession.query(Source.histology.distinct().label('histology')).filter(
        Source.histology == request.params["search_all"]).all())
    result["organ"] = json.dumps(DBSession.query(Source.organ.distinct().label('organ')).filter(
        Source.organ == request.params["search_all"]).all())
    result["organism"] = json.dumps(DBSession.query(Source.organism.distinct().label('organism')).filter(
        Source.organism == request.params["search_all"]).all())
    result["celltype"] = json.dumps(DBSession.query(Source.celltype.distinct().label('celltype')).filter(
        Source.celltype == request.params["search_all"]).all())
    result["person"] = json.dumps(DBSession.query(Source.person.distinct().label('person')).filter(
        Source.person == request.params["search_all"]).all())
    result["location"] = json.dumps(DBSession.query(Source.location.distinct().label('location')).filter(
        Source.location == request.params["search_all"]).all())

    result["treatment"] = json.dumps(DBSession.query(Source.treatment.distinct().label('treatment')).filter(
        Source.treatment == request.params["search_all"]).all())

    # Search HLA
    result["hla"] = json.dumps(DBSession.query(HlaType.hla_string.distinct().label('hla')).filter(
        HlaType.hla_string == request.params["search_all"]).all())
    # Search MS_run
    result["msrun"] = json.dumps(DBSession.query(MsRun.filename.distinct().label('msrun')).filter(
        MsRun.filename == request.params["search_all"]).filter(MsRun.flag_trash ==0).all())
    # Search Protein
    result["protein"] = json.dumps(DBSession.query(Protein.name.distinct().label('protein')).filter(
        Protein.name == request.params["search_all"]).all())
    # Search Protein with gene name
    if result["protein"] == "[]":
        result["protein"] = json.dumps(DBSession.query(Protein.name.distinct().label('protein')).filter(
            Protein.gene_name == request.params["search_all"]).all())

        # except:
        # return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return result