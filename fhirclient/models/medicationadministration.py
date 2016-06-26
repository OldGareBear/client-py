#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2016-06-26.
#  2016, SMART Health IT.


from . import domainresource

class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.
    
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    
    resource_name = "MedicationAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        
        self.effectiveTimeDateTime = None
        """ Start and end time of administration.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectiveTimePeriod = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `MedicationAdministrationEventHistory` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ What was administered.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the administration.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who received medication.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who administered substance.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Order administration performed against.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.reasonGiven = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
        
        self.wasNotGiven = None
        """ True if medication not administered.
        Type `bool`. """
        
        super(MedicationAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
            ("effectiveTimeDateTime", "effectiveTimeDateTime", fhirdate.FHIRDate, False, "effectiveTime", True),
            ("effectiveTimePeriod", "effectiveTimePeriod", period.Period, False, "effectiveTime", True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("eventHistory", "eventHistory", MedicationAdministrationEventHistory, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("reasonGiven", "reasonGiven", codeableconcept.CodeableConcept, True, None, False),
            ("reasonNotGiven", "reasonNotGiven", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("wasNotGiven", "wasNotGiven", bool, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    
    resource_name = "MedicationAdministrationDosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dose = None
        """ Amount of medication per dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.method = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ Dose quantity per unit of time.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteCodeableConcept = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Body site administered to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("dose", "dose", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False, "site", False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False, "site", False),
            ("text", "text", str, False, None, False),
        ])
        return js


class MedicationAdministrationEventHistory(backboneelement.BackboneElement):
    """ A list of events of interest in the lifecycle.
    
    A summary of the events of interest that have occurred, such as when the
    administration was verified.
    """
    
    resource_name = "MedicationAdministrationEventHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Action taken (e.g. verify).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ Who took the action.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ The date at which the event happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reason = None
        """ Reason the action was taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
        
        super(MedicationAdministrationEventHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationEventHistory, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import ratio
