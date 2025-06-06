# Convert qref dialect to qir dialect
# Only simple gates are converted; qref.dyn_gate is skipped.

from inconspiquous.dialects import qref
from inconspiquous.dialects import qir
from inconspiquous.dialects.qref import GateOp, MeasureOp as QrefMeasureOp, DynGateOp

# This is a stub. Actual integration with xDSL IR will require more work.
def convert_qref_to_qir(qref_module):
    """
    Convert a qref dialect module to a qir dialect module, skipping dyn_gate ops.
    """
    from inconspiquous.dialects.qir import HOp, XOp, CNOTOp, MeasureOp as QirMeasureOp
    qir_ops = []
    for op in qref_module.ops:
        if isinstance(op, GateOp):
            # TODO: Map gate type to QIR op (H, X, CNOT, etc.)
            # For now, just append HOp as a placeholder
            qir_ops.append(HOp())
        elif isinstance(op, QrefMeasureOp):
            qir_ops.append(QirMeasureOp())
        elif isinstance(op, DynGateOp):
            continue  # skip dynamic gates
        # ...add more ops as needed...
    # Return a new qir module
    return type('QIRModule', (), {'ops': qir_ops})()
