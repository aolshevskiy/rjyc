import sbt._

import java.io.File

class RJyCProject(info: ProjectInfo) extends DefaultProject(info) with JythonPaths with JavaProject {
  var sakaiRepo = "SakaiProject Repository" at "http://source.sakaiproject.org/maven2/"
  val jython = "org.python" % "jython-complete" % "2.5.1"

  override def managedStyle = ManagedStyle.Maven

  override def testResources =
    testJythonResources +++ super.testResources

  override def mainResources = 
    super.mainResources +++
    mainJythonResources

  override def ivyRepositories = Resolver.withDefaultResolvers(repositories.toSeq, false)
  
  var publishTo = Resolver.file("Local Maven repository", new java.io.File(Path.userHome+"/projects/maven2/maven2"))
}
